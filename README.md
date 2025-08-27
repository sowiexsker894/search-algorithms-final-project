# 🚀 **Search Algorithms: Optimal Route Finder**

> **Advanced Graph Theory Implementation for Supply Chain Optimization**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![NetworkX](https://img.shields.io/badge/NetworkX-2.8+-green.svg)](https://networkx.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.5+-orange.svg)](https://matplotlib.org/)
[![Tkinter](https://img.shields.io/badge/Tkinter-GUI-yellow.svg)](https://docs.python.org/3/library/tkinter.html)

## 📋 **Project Overview**

This project implements three fundamental search algorithms to solve complex supply chain routing problems:

- **🔄 Kruskal's Algorithm** - Minimum Spanning Tree for optimal network design
- **🎯 Dijkstra's Algorithm** - Shortest path finding in weighted graphs  
- **🌊 Ford-Fulkerson Algorithm** - Maximum flow optimization for supply networks

## ✨ **Key Features**

- **Interactive GUI** built with Tkinter for seamless user experience
- **Real-world dataset integration** with CSV files for practical applications
- **Visual graph representation** using NetworkX and Matplotlib
- **Multi-algorithm comparison** for different optimization scenarios
- **Cost analysis** and route optimization for supply chain management

## 🏗️ **Architecture**

```
search-algorithms-final-project/
├── tf_complejidad/
│   └── Pandasapp/
│       ├── gui.py              # Main GUI interface
│       ├── kruskal.py          # Kruskal's MST algorithm
│       ├── dikstra.py          # Dijkstra's shortest path
│       ├── fulkerson.py        # Ford-Fulkerson max flow
│       ├── main.py             # Application entry point
│       └── dataset/            # CSV data files
│           ├── DATASETNODOSYCALLES.csv
│           ├── Costominimo_por_id.csv
│           └── CAPACIDADESMAXIMASENLASCALLES.csv
```

## 🚀 **Getting Started**

### Prerequisites
```bash
pip install networkx matplotlib pandas tkinter
```

### Running the Application
```bash
cd tf_complejidad/tf_complejidad/Pandasapp
python gui.py
```

## 📊 **Algorithms Implemented**

### 1. **Kruskal's Algorithm** 🌳
- **Purpose**: Find minimum spanning tree for optimal network connectivity
- **Use Case**: Design cost-effective supply chain networks
- **Output**: Minimum cost maintenance routes with visual representation

### 2. **Dijkstra's Algorithm** 🎯
- **Purpose**: Find shortest path between two nodes in weighted graphs
- **Use Case**: Optimize delivery routes and minimize travel time
- **Output**: Optimal path visualization with cost analysis

### 3. **Ford-Fulkerson Algorithm** 🌊
- **Purpose**: Calculate maximum flow through network capacities
- **Use Case**: Optimize supply chain throughput and bottleneck identification
- **Output**: Flow network analysis with capacity constraints

## 🎨 **User Interface**

The application features a modern, intuitive GUI with:
- **Interactive buttons** for each algorithm
- **Real-time graph visualization** 
- **Cost analysis displays**
- **Professional branding** for "BODEGA UNO"

## 📈 **Performance & Complexity**

| Algorithm | Time Complexity | Space Complexity | Best For |
|-----------|----------------|------------------|----------|
| Kruskal   | O(E log E)     | O(V + E)        | Network Design |
| Dijkstra  | O(V²)          | O(V)            | Shortest Path |
| Ford-Fulkerson | O(VE²)   | O(V²)           | Max Flow |

## 🔧 **Technical Implementation**

- **Graph Representation**: NetworkX library for efficient graph operations
- **Data Processing**: Pandas for CSV file handling and data manipulation
- **Visualization**: Matplotlib for professional graph plotting
- **GUI Framework**: Tkinter for cross-platform compatibility

## 📁 **Dataset Structure**

The application works with structured CSV data containing:
- **Node information**: Geographic coordinates and identifiers
- **Edge weights**: Cost and capacity constraints
- **Street names**: Human-readable location descriptions

## 🎯 **Use Cases**

- **Supply Chain Optimization**: Minimize transportation costs
- **Network Design**: Create efficient infrastructure layouts
- **Route Planning**: Optimize delivery and service routes
- **Capacity Planning**: Analyze network bottlenecks and flows

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 **Author**

- **Nicole Sihuincha** - - [Search Algorithms Project](https://github.com/yourusername/search-algorithms-final-project)

## 🙏 **Acknowledgments**

- **NetworkX** team for excellent graph theory library
- **Matplotlib** for powerful visualization capabilities
- **Python community** for robust ecosystem and tools

---

⭐ **Star this repository if you find it helpful!**

🔗 **Connect with us**: [GitHub](https://github.com/sowiexsker894) | [LinkedIn](https://linkedin.com/in/nicoleschermacha)
