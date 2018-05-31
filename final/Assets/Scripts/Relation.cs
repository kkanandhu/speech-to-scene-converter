using UnityEngine;
using System.Collections;
using System;
using System.Collections.Generic;
public class Relation : MonoBehaviour {
public  Prepo pr;
float pheight;
float pwidth;
float plenghth;
float cheight;
float cwidth;
float clenghth;
float tolerance;
GameObject parent;
GameObject child;
	string pname;

	char[] lastchar;
public void relate()
{


		try {
		
		if (pr.mySplit [1] != ".") {
			
			Debug.Log ("relations");

		
			string[] parts = pr.mySplit [1].Split (' ');
			string[] left = parts [0].Split ('.');
			string[] right = parts [2].Split ('.');
			

				//WORKSPACE

				switch (parts [1]) {

				case "on":

					//NUMBER Debug.Log (right [0]);
					//ITEM Debug.Log (right [1]);
					tolerance=0;
					List<GameObject> childs = new List<GameObject>();
					int x=Int32.Parse(left [0]);
					lastchar = right[1].TrimEnd().ToCharArray();

					if(!Char.IsNumber(lastchar[0]))
					{
						pname=right[1]+"1";
					}

					for(int i=0;i<x;i++)
					{
					Debug.Log(pname);
					string cname=left[1]+(i+1).ToString();
						parent= GameObject.Find (pname);
					child=GameObject.Find (cname);
					
					pheight = parent.GetComponent<Renderer> ().bounds.size.y;
					cheight = child.GetComponent<Renderer> ().bounds.size.y;
					child.transform.position+= new Vector3 (0,pheight, 0);
					childs.Add(child);
					}
					break;
				

				case "near":

				//NUMBER Debug.Log (right [0]);
				//ITEM Debug.Log (right [1]);
				tolerance=0;
				x=Int32.Parse(left [0]);

				lastchar = right[1].TrimEnd().ToCharArray();

				if(!Char.IsNumber(lastchar[0]))
				{
					pname=right[1]+"1";
				}

				for(int i=0;i<x;i++)
				{
					Debug.Log(pname);
					string cname=left[1]+(i+1).ToString();
					parent= GameObject.Find (pname);
					child=GameObject.Find (cname);

					pwidth = parent.GetComponent<Renderer> ().bounds.size.z;
					cwidth = child.GetComponent<Renderer> ().bounds.size.z;
						child.transform.position+= new Vector3 (0,pheight,pwidth+cwidth);
				
				}
				break;
				}
				//WORKSPACE
		

	
		} 
		} catch (System.Exception ae) {

		}
}
}
