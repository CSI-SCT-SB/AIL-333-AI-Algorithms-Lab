#331_gadha lekshmi p
# exp2_water jug

visited=[]
queue=[]
operations=['fill_left','fill_right','empty_left','empty_right','trans_left','trans_right']
queue.append('0')
queue.append('0')

x=int(input('enter max capacity of jug1 '))
y=int(input('enter max capacity of jug2 '))
g=int(input('enter goal node '))
while len(queue)!=0:
		lcurr=int(queue.pop(0))
		rcurr=int(queue.pop(0))
		if((lcurr > x or rcurr > y or lcurr < 0 or rcurr <0)):
				continue
		if[lcurr,rcurr] not in visited:
					print([lcurr,rcurr])
					visited.append([lcurr,rcurr])
					
					if ((lcurr== g and rcurr==0) or (lcurr == 0 and rcurr == g)) :
								print('goal found')
								break
					for option in operations :
							if option== 'fill_left':
										temp_left=x
										temp_right=rcurr
							elif option== 'fill_right':
										temp_left=lcurr
										temp_right=y
							elif option== 'empty_left':
										temp_left=0
										temp_right=rcurr
							elif option== 'empty_right':
										temp_left=lcurr
										temp_right=0
							elif option=='trans_left':
									z=int(lcurr+rcurr)
									if(z>x):
												temp_left=x
												temp_right=z-x
									else:
												temp_left=z
												temp_right=0
							elif option=='trans_right' :
									z=int(lcurr+rcurr)
									if(z>y):
												temp_left=z-y
												temp_right=x
									else :
												temp_left=z
												temp_right=0
							queue.append(temp_left)
							queue.append(temp_right)
					
