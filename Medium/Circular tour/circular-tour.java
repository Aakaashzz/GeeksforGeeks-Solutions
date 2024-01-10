//{ Driver Code Starts
import java.util.*;


class First_Circular_tour
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int t =sc.nextInt();
		while(t>0)
		{
			int n = sc.nextInt();
			sc.nextLine();
			String str = sc.nextLine();
			String arr[] = str.split(" ");
			int p[] = new int[n];
			int d[] = new int[n];
			int j=0;
			int k=0;
			for(int i=0; i<2*n; i++)
			{
				if(i%2 == 0)
				{
					p[j]= Integer.parseInt(arr[i]);
					j++;
				}
				else
				{
					d[k] = Integer.parseInt(arr[i]);
					k++;
				}
			}
			
			System.out.println(new Solution().tour(p,d));
		t--;
		}
	}
}
// } Driver Code Ends


// In java function tour() takes two arguments array of petrol
// and array of
class PetrolPump {
    int petrol;
    int distance;
    
    public PetrolPump(int petrol, int distance) {
        this.petrol = petrol;
        this.distance = distance;
    }
}

class Solution {
    int tour(int petrol[], int distance[]) {
        int n = petrol.length;
        int start = 0;
        int balance = 0;
        int total = 0;

        for (int i = 0; i < n; i++) {
            int diff = petrol[i] - distance[i];
            total += diff;
            balance += diff;

            if (balance < 0) {
                start = i + 1;
                balance = 0;
            }
        }
        return (total >= 0) ? start : -1;
    }
}