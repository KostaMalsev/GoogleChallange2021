

sum = i=0; 
a3=0; 
a1=1;
a2=1;
 
while(i <= 164)
{ 
	a3 = a1+a2;
	 	
	if(i % 2 == 0)
	{
		sum +=a3;
	}
	
	a1 = a2;
	a2=a3;
	i++
	
}

console.log(sum.toString())
	
	
