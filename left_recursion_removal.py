def main():
        '''
        give inputs like A->Ab | c
        that'll slve for left recursion

        give inputs like A->B | E
        test your self.
        '''
        
        s = input('enter string:')
        t,res = s.split('->')
	
        fact1,fact2 = res.split('|')
        if t==fact1[0] or t == fact2[0]:
                if t in fact2:
                        fact1,fact2 = fact2,fact1
		
                rep = t + "'"
	
                print(t,'->',fact2,rep)
                
                if len(fact1)>1:
                        print(rep,'->',fact1[1],rep)
                else:
                        print(rep,'->',rep)
        else:
                print('no recursion')

if __name__ == '__main__':
	main()
