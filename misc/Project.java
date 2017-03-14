import java.io.*;
import java.util.*;

public class Project
{
	public static void main(String args[])
	{
		int count=0;
		Double w=Math.random();
		Double t=0.0;
		Scanner in=new Scanner(System.in);
		System.out.println("Enter distance");
		Double d=in.nextDouble();
		int flag=0;
		do
		{
		
		
		count++;
	
		System.out.println("Weight= "+w);
		
		for(Double i=d;i>0 && flag==0;i=i-0.5)
		{
			
			Double m=i*w;
			System.out.println("Multiply= "+m);
			if(m<t && i==1.5)
			{
				System.out.println("Stopped at d="+i);
				flag=1;
			}
		}	
		if(flag==0)
		{
			t=t+0.1;
			System.out.println("t="+t);
		}	
		}while(flag==0);
		System.out.println("count="+count);	
		
	}
}