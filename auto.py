from main import Main
import csv

with open('data.csv', mode='w') as data:
    f = csv.writer(data, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    f.writerow(['SIZE_PROBLEM', 'N_STEPS', '', 'IDS_time', 'IDS_nodes', 'BFS_time', 'BFS_nodes', 'BFS_BI_time', 'BFS_BI_nodes', 'A_time', 'A_nodes', 'A Optimized_time', 'A Optimized_nodes'])

    

t = Main(no_graph=True, no_diagram_tree=True)
result = t.solve()

test = [[9,5, 500],[9,10, 500],[9,15, 50],
        [16,5,100],[16,10,100],
        [25,5,100],[25,10,100]]

for e in test:

    for i in range(e[2]):
        t.set_new(e[0],e[1])
        print("\n\nCALCULATING %s] %s size %s steps" % (str(i)+"/"+str(e[2]), e[0],e[1]))
        result = t.solve()

        with open('data.csv', mode='a') as data:
            f = csv.writer(data, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator="\n")

            IDS = result['IDS']
            BFS = result['BFS']
            BFS_bi = result['BFS_bidirectional']
            A_star = result['A_star']
            Opt_A_star = result['Optimized_A_star']

            f.writerow([t.size_problem, t.n_steps, '', 
                IDS['time'], IDS['exp_nodes'], 
                BFS['time'], BFS['exp_nodes'], 
                BFS_bi['time'], BFS_bi['exp_nodes'],
                A_star['time'], A_star['exp_nodes'], 
                Opt_A_star['time'], Opt_A_star['exp_nodes']
                ])
    
    
