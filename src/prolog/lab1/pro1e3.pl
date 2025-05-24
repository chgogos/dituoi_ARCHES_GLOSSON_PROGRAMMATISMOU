parent(a,b).
parent(a,c). 
parent(b,d). 
parent(b,e).  
parent(c,f).  

sibling(X,Y) :- parent(Z,X), parent(Z,Y), not(X=Y).
cousin(X,Y) :- parent(Z,X), parent(W,Y), sibling(Z,W). 
grandchild(X,Y) :- parent(Z,X), parent(Y,Z).
descendent(X,Y) :- parent(Y,X).
descendent(X,Y) :- parent(Z,X), descendent(Z,Y).
