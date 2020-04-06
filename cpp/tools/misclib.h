#include <bits/stdc++.h>
#include <variant>

template<typename _collection, typename _item>
bool has(_collection c, _item i){
    return c.find(i) != c.end();
}

template<typename _NodeReference>
class TreePrinter {
private:

    typedef std::function<std::vector<_NodeReference>(_NodeReference)> NeighborGetter;
    typedef std::function<std::string(_NodeReference)> LabelGetter;

    NeighborGetter get_neighbors;
    LabelGetter get_label;
    _NodeReference root;
    std::unordered_map<_NodeReference, int> minimum_width;
    std::unordered_map<_NodeReference, int> depth;

    int get_minimum_width(_NodeReference root){
        auto m = minimum_width.find(root);
        if (m != minimum_width.end()) return m->second;
        auto neighbor = get_neighbor(root);
        int num_neighbor = 0;
        std::size_t width = 0;
        for (auto &c: neighbor){
            if (!has(depth, c)){
                depth[c] = depth[root] + 1;
                width += get_minimum_width(c);
                num_neighbor += 1;
            }
        }
        width += std::max(num_neighbor - 1, 0);
        std::string label = get_label(root);
        width = std::max(width, label.size());
        minimum_width[root] = width;
        return width;
    }

    std::string print_label_with_width(_NodeReference n, int width){
        std::string label = get_label(n);
        std::string rv;
        width -= label.size();
        for (int i = 0; i < width/2; i++) rv += " ";
        rv += label;
        for (int i = 0; i < width - width/2; i++) rv += " ";
        return rv;
    }

    void print(_NodeReference root, int width){
        std::unordered_set<_NodeReference> visited;
        visited.insert(root);
        std::vector<std::string> lines;
        typedef std::variant<std::pair<_NodeReference,int>, int> Cell;
        std::vector<Cell> current_line ({
            Cell(std::in_place_index<0>,root, width)});
        std::vector<Cell> next_line;
        int last_depth = 0;
        while (!current_line.empty()){
            int real_nodes = 0;
            for (auto var: current_line){
                if (auto _node = std::get_if<0>(&var)){
                    real_nodes ++;
                }
            }
            if (real_nodes == 0){
                break;
            }
            lines.push_back(std::string("|"));
            for (int i = 0; i < current_line.size(); i++){
                if (auto x = std::get_if<0>(&current_line[i])){
                    _NodeReference node = x->first;
                    int w = x->second;
                    int sum_w_neighbor = 0;
                    auto neighbor = get_neighbor(node);
                    for (auto c: neighbor){
                        if (visited.find(c) == visited.end ()){
                            sum_w_neighbor += minimum_width[c] + 1;
                        }
                    }
                    int extra_spaces = w - sum_w_neighbor + 1;
                    int added_neighbor = 0;
                    for (int i = 0; i < neighbor.size(); i++){
                        _NodeReference c = neighbor[i];
                        int extra = extra_spaces/current_line.size() + (i < (extra_spaces % current_line.size()));
                        if (visited.find(c) == visited.end ()){
                            next_line.push_back(Cell(std::in_place_index<0>,c,minimum_width[c] + extra));
                            added_neighbor ++;
                        }
                        visited.insert(c);
                    }
                    if (added_neighbor == 0){
                        next_line.push_back(Cell(std::in_place_index<1>, w));
                    }
                    lines.back() += print_label_with_width(node, w);
                }
                else {
                    int w = std::get<1>(current_line[i]);
                    for (int i = 0; i < w; i++) lines.back() += " ";
                    next_line.push_back(current_line[i]);
                }
                lines.back() += "|";
            }
            current_line.swap(next_line);
            next_line.clear();
        }

        for (auto line: lines){
            std::cout << line << std::endl;
        }
    }

    public:

    TreePrinter(NeighborGetter ng, LabelGetter lg, _NodeReference r){
        get_neighbor = ng;
        get_label = lg;
        root = r;
        depth[r] = 0;
    }

    void print(){
        print(root, get_minimum_width(root));
    }
};

template <typename _NodeReference>
class GraphPrinter {
    private:

    public:
    TreePrinter(NeighborGetter ng, LabelGetter lg, _NodeReference r){
        get_neighbor = ng;
        get_label = lg;
        root = r;
        depth[r] = 0;
    }
    
    void print(){
        print(root, get_minimum_width(root));
    }
};