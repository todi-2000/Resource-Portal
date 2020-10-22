# include<stdio.h>

void sortedknapsack(int n,float weight[], float cost[])
{
    float ratio[n], temp;
    for (int i = 0; i <n; i++) {
      ratio[i] = cost[i] / weight[i];
   }
   for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
         if (ratio[i] < ratio[j]) {
            temp = ratio[j];
            ratio[j] = ratio[i];
            ratio[i] = temp;

            temp = weight[j];
            weight[j] = weight[i];
            weight[i] = temp;

            temp = cost[j];
            cost[j] = cost[i];
            cost[i] = temp;
         }
      }
   }
}

void knapsack(int n, float weight[], float cost[], float value) {
   float x[n], total = 0,selectedcost[n];
   float W=0;

   for (int i = 0; i < n; i++)
      x[i] = 0.0;
   int i=-1;
   while(W<value && i<n)
   {
       i++;
       if(W+weight[i]<=value)
       {
           x[i]=1.0;
           W+=weight[i];
           total+=cost[i];
           selectedcost[i]=cost[i];
       }
       else
       {
           x[i]=(value-W)/weight[i];
           W=value;
           total+=(cost[i]*x[i]);
           selectedcost[i]=(cost[i]*x[i]);
       }
   }
   printf("\n\nValue of x[i] are: ");
   for(int j=0;j<n;j++)
        printf("%f ",x[j]);
   printf("\n\nCost selected: ");
   for(int j=0;j<=i;j++)
        printf("%f ",selectedcost[j]);
   printf("\n\nTotal cost: %f",total);
}

void main() {
   int n;
   printf("Enter the number of items: ");
   scanf("%d",&n);
   float weight[n], cost[n],value;
   printf("\nEnter the profits of each object:- ");
   for (int i = 0; i < n; i++) {
      scanf("%f",&cost[i]);
   }
   printf("\nEnter the wts of each object: ");
   for (int i = 0; i < n; i++) {
      scanf("%f", &weight[i]);
   }
   printf("\nEnter the capacity of knapsack:- ");
   scanf("%f", &value);
   sortedknapsack(n,weight,cost);
   printf("\nSorted profits of each object:- ");
   for (int i = 0; i < n; i++) {
      printf("%f ",cost[i]);
   }
   printf("\n\nSorted wts of each object: ");
   for (int i = 0; i < n; i++) {
      printf("%f ",weight[i]);
   }
   knapsack(n, weight, cost, value);
}
