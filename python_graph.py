from collections import defaultdict,deque


class Graph:
  
    def __init__(self):
        self.vertices= defaultdict(list)#No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph

        self.obrnut_graph=defaultdict(list)
        self.count=0
        self.komponente=defaultdict(list)

        self.slabe_komponente=defaultdict(list)
        
        self.obrnute_komponente=defaultdict(list)
        self.finalne_komponente=defaultdict(list)

        self.lista_posjecenih=[]
  
    # function to add an edge to graph
    def addEdge(self,u,v):
        #temp = (u,v)
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def print_graph(self):
        for key in self.graph.keys():
            #print "%s: %s" % (self.vertices[key], self.graph[key])
            print "%s: %s" % (key, self.graph[key])
            
            
            
        
        
    def read_graph_pajek(self,text):
        edgeDataStarts='false';
        with open(text) as file:
            for line in file:
                s=line.split()
                if s[0]=='*edges':
                    break
                if s[0]=='*vertices':
                    continue
                if s[0]=='*arcs': 
                    edgeDataStarts='true'
                    continue
                if edgeDataStarts=='false':             
                    self.vertices[int(s[0])] = s[1].strip('"')
                    self.graph[int(s[0])]=[]
                else:
                    self.addEdge(int(s[0]),int(s[1]))
                    """
                    if int(s[0]) not in self.__graph_dic:
                        self.__graph_dic[int(s[0])]=[int(s[1])]
                    else:
                        self.__graph_dic[int(s[0])].append(int(s[1]))
                    """
                   
    
    def pronadi_komponente(self):
        self.lista_posjecenih=[]
        counter=0

        for key in self.vertices.keys():
            if key in self.lista_posjecenih:
                continue
            path=[]
            start=[key]
            path=self.iterative_dfs(start)
            #path.insert(0, key)
            for values in path:
                if values not in self.lista_posjecenih:
                    self.lista_posjecenih.append(values)
                else:
                    path.remove(values)
            #print path
            counter=counter+1
            #if len(path)>1:
            self.komponente[key]=path

    def pronadi_obrnute_komponente(self):
        self.lista_posjecenih = []
        counter = 0

        for key in self.vertices.keys():
            if key in self.lista_posjecenih:
                continue
            path = []
            start = [key]
            path = self.iterative_dfs(start)
            # path.insert(0, key)
            for values in path:
                if values not in self.lista_posjecenih:
                    self.lista_posjecenih.append(values)
                else:
                    path.remove(values)
                # print path
            counter = counter + 1
            # if len(path)>1:
            self.obrnute_komponente[key]=path

    def iterative_dfs(self, start):
        q=deque(start)
        path=[]

        while q:
            v=q.popleft()
            if v not in path:
                path.append(v)
                q.extendleft(reversed(self.graph[v]))

        return path

    def iterative_dfss(self, start):
        q=deque(start)
        path=[]

        while q:
            v=q.popleft()
            if v not in path:
                path.append(v)
                q.extendleft(reversed(self.obrnut_graph[v]))

        return path
            
         
    def ispis_komponenti(self):
        #print self.count

        for key in self.komponente.keys():
            print "%s: %s" % (key, self.komponente[key])
            
    def definiraj_komponente(self):
        
        for key in self.komponente.keys():
            temp=self.komponente[key]
            temp2=self.obrnute_komponente[key]
            temp3=[]
            
            for values in temp:
                temp3.append(values)
            for values in temp2:
                if values not in temp3:
                    temp3.append(values)
            self.finalne_komponente[key]=temp3


            
    def ispis_count(self):
        temp = 0

        for key in self.komponente.keys():
            if len(self.finalne_komponente[key])!=0:
                self.count = self.count + 1

        print self.count


    def ispis_svega(self):
        print len(self.komponente)
    
    def max_komponenta(self):
        temp=0
        for key in self.finalne_komponente.keys():
            temp2=len(self.finalne_komponente[key])
            if temp < temp2:
                temp=temp2
        
        return temp
            
            

if __name__ == "__main__":
    
    
    g=Graph()
    g.read_graph_pajek("eva.net")
    #g.print_graph()

    g.pronadi_komponente()
    g.pronadi_obrnute_komponente
    g.definiraj_komponente()
    g.ispis_komponenti()
    g.ispis_count()
    #g.ispis_svega()
    #temp=g.max_komponenta()


    
    
                        
        