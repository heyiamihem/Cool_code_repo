#include<bits/stdc++.h>
using namespace std;

class Node{
	public:
	int data;
	Node * next;
}*first=NULL;

int count(Node *p)
{
	int count=0;
	while(p)
	{
		count++;
		p=p->next;
	}
	return count;
}

void reverse(Node *p)
{
    // p=first;
	Node *q=NULL;
	Node *r=NULL;
	
	while(p)
	{
		r=q;
		q=p;
		p=p->next;
		q->next=r;
	}
	first=q;
	
	}

void insert(Node *p,int pos,int value)
{
	Node *t;
	t=new Node;
	if(pos==0)
	{
		
		t->data=value;
		t->next=first;
		first=t;
	}
	else{
	
	for(int i=0;i<pos-1;i++)
	{
		p=p->next;
	}

	t->data=value;
	t->next=p->next;
	p->next=t;
}
	
}

void display(Node * p)
{
	while(p!=NULL)
	{
		cout<<p->data<<" ";
		p=p->next;
	}
}

int delet( Node * p,int pos)
{
	Node *q;
	int x;
	if(pos==1)
	{
	 q=first;
	 first=first->next;
	  x=q->data;
	 delete q;
	 return x;
	 	
	}
	
	else
	{
		for(int i=0;i<pos-1;i++)
		{
			q=p;
			p=p->next;
			
		}
		q->next=p->next;
		x=p->data;
		delete p;
		return x;
	}
}

int main()
{
	insert(first,0,1);
	insert(first,1,2);
	insert(first,2,3);
	display(first);
	reverse(first);
	display(first);
	cout<<endl<<count(first)<<endl;
	delet(first,2);
	display(first);
}
