import tkinter as tk
from tkinter import messagebox
from search_algo import *

class SearchAlgorithmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Search Algorithms")
        self.root.geometry("400x400")  # Adjust window size
        self.graph = {}

        # Create buttons and add them to the window
        self.create_buttons()

        # Create a Listbox to display the path
        self.path_listbox = tk.Listbox(self.root, width=50, height=10, font=("Arial", 12))
        self.path_listbox.pack(pady=20)

    def create_buttons(self):
        btn_bfs = tk.Button(self.root, text="Breadth First Search", width=30, command=self.breadth_first_search)
        btn_bfs.pack(pady=5)

        btn_ucs = tk.Button(self.root, text="Uniform Cost Search", width=30, command=self.uniform_cost_search)
        btn_ucs.pack(pady=5)

        btn_dfs = tk.Button(self.root, text="Depth-first search (DFS)", width=30, command=self.depth_first_search)
        btn_dfs.pack(pady=5)

        btn_dls = tk.Button(self.root, text="Depth-limited search", width=30, command=self.depth_limited_search)
        btn_dls.pack(pady=5)

        btn_ids = tk.Button(self.root, text="Iterative Deepening Search (IDS)", width=30, command=self.iterative_deepening_search)
        btn_ids.pack(pady=5)

        btn_astar = tk.Button(self.root, text="A* Search", width=30, command=self.a_star_search)
        btn_astar.pack(pady=5)

        btn_greedy = tk.Button(self.root, text="Greedy Best First Algorithm", width=30, command=self.greedy_best_first_algorithm)
        btn_greedy.pack(pady=5)

    def draw_path(self, path):
        self.path_listbox.delete(0, tk.END)
        for i in range(len(path) - 1):
            self.path_listbox.insert(tk.END, f"{path[i]} --> {path[i+1]}")
        
        if len(path) == 1:
            self.path_listbox.insert(tk.END, f"{path[0]}")

    def breadth_first_search(self):
        self.graph = {
            "المرج": ["الشهداء"],
            "الشهداء": ["شبرا الخيمة", "عرابى", "العتبه"],
            "شبرا الخيمة": [],
            "عرابى": ["ناصر"],
            "العتبه": ["عدلى منصور"],
            "ناصر": ["الكيت كات", "السادات", "العتبه", "الشهداء"],
            "السادات": ["العتبه", "جامعة القاهرة", "حلوان"],
            "الكيت كات": ["جامعة القاهرة", "محور روض"],
            "محور روض": [],
            "جامعة القاهرة": ["المنيب"],
            "حلوان": [],
            "المنيب": []
        }
        path = bfs(self.graph, "المرج", "المنيب")
        self.draw_path(path)

    def uniform_cost_search(self):
        self.graph = {
            "المرج": [("الشهداء", 12)],
            "الشهداء": [("شبرا الخيمة",7), ("عرابى",1), ("العتبه",1)],
            "شبرا الخيمة": [],
            "عرابى": [("ناصر",1)],
            "العتبه": [("عدلى منصور",18)],
            "ناصر": [("الكيت كات",3), ("السادات",1), ("العتبه",1), ("الشهداء",3)],
            "السادات": [("العتبه",1), ("جامعة القاهرة",4), ("حلوان",18)],
            "الكيت كات": [("جامعة القاهرة",5), ("محور روض",6)],
            "محور روض": [],
            "جامعة القاهرة": [("المنيب",5)],
            "حلوان": [],
            "المنيب": []
        }
        path = ucs(self.graph, "المرج","المنيب")
        cost,__ = cost_path_uniform(path)
        path.append(cost)
        self.draw_path(path)  

    def depth_first_search(self):
        self.graph = {
            "المرج": ["الشهداء"],
            "الشهداء": ["شبرا الخيمة", "عرابى", "العتبه"],
            "شبرا الخيمة": [],
            "عرابى": ["ناصر"],
            "العتبه": ["عدلى منصور"],
            "ناصر": ["الكيت كات", "السادات", "العتبه", "الشهداء"],
            "السادات": ["العتبه", "جامعة القاهرة", "حلوان"],
            "الكيت كات": ["جامعة القاهرة", "محور روض"],
            "محور روض": [],
            "جامعة القاهرة": ["المنيب"],
            "حلوان": [],
            "المنيب": []
        }
        path = dfs(self.graph, "المرج", "المنيب")
        self.draw_path(path)

    def depth_limited_search(self):
        self.graph = {
            "المرج": ["الشهداء"],
            "الشهداء": ["شبرا الخيمة", "عرابى", "العتبه"],
            "شبرا الخيمة": [],
            "عرابى": ["ناصر"],
            "العتبه": ["عدلى منصور"],
            "ناصر": ["الكيت كات", "السادات", "العتبه", "الشهداء"],
            "السادات": ["العتبه", "جامعة القاهرة", "حلوان"],
            "الكيت كات": ["جامعة القاهرة", "محور روض"],
            "محور روض": [],
            "جامعة القاهرة": ["المنيب"],
            "حلوان": [],
            "المنيب": []
        }
        path = dls(self.graph, "المرج", "المنيب",7)
        print(path)
        self.draw_path(path)

    def iterative_deepening_search(self):
        self.graph = {
            "المرج": ["الشهداء"],
            "الشهداء": ["شبرا الخيمة", "عرابى", "العتبه"],
            "شبرا الخيمة": [],
            "عرابى": ["ناصر"],
            "العتبه": ["عدلى منصور"],
            "ناصر": ["الكيت كات", "السادات", "العتبه", "الشهداء"],
            "السادات": ["العتبه", "جامعة القاهرة", "حلوان"],
            "الكيت كات": ["جامعة القاهرة", "محور روض"],
            "محور روض": [],
            "جامعة القاهرة": ["المنيب"],
            "حلوان": [],
            "المنيب": []
        }
        path = ids(self.graph, "المرج", "المنيب")
        print(path)
        self.draw_path(path)

    def a_star_search(self):#
        self.graph = {
    'S': [('A',1),('B',4)],
    'A': [('B',2),('C',5),('G',12)],
    'B': [('C',2)],
    'C': [('G',3)],
    'G': [],
                    }

        nodes = {
    'S':7,
    'A':6,
    'B':4,
    'C':2,
    'G':0,
}

        path = a_star_search(self.graph, 'S', 'G')
        
        cost,__ = cost_path(path)
        path.append(cost)
        self.draw_path(path)
    def greedy_best_first_algorithm(self):
        self.graph = {
    'S': [(2,'A'),(3,'B'),(5,'D')],
    'A': [(4,'C')],
    'B': [(5,'D')],
    'D': [(0,'G')],
    'C': [(5,'D'),(0,'G')],
    'G': [],
}
        path = gbfs(self.graph, "S", "G")
        print(path)
        self.draw_path(path)



root = tk.Tk()
app = SearchAlgorithmApp(root)


root.mainloop()
