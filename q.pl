:-module(q,[main/1]). :-use_module(library(dcg/basics)). +[A/P|S]-->[0'(],integer(A),[0'/],integer(P),[0')],(+S;{S=[]}). \[]. \[H|T]:- \+ member(H,T),\T. 1-0. 0-1. []*I*H*V:-reverse(H,X),append(X,V,S),reverse(S,D),atomics_to_string(D,E),writeln(E),(V=[0|_];I*I*H*V). [0|R]*I*H*V:-(H=[],B=1,F=H;H=[A|F],A-B),R*I*F*[B|V]. [1|R]*I*H*[A|V]:-(A=1,G=[A|H],F=V;G=H,F=[A|V]),R*I*G*F. [2,F|R]*I*H*[A|V]:-(A=0,S=[F|R];S=R),S*I*H*[A|V]. main([C]):-open(C,read,Q),read_string(Q,_,Z),string_codes(Z,T),close(Q),+(F,T,[]),\F,maplist([A/P,L]>>(J is A^((P-1)/2)mod P,(J is P-1->L=2;L=J)),F,G),G*G*[]*[0].



