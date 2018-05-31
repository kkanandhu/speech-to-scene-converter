using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System.IO;


public class Load : MonoBehaviour {


	public string line;
	string ur="localhost/Bundles/Windows/";
	Vector3 Stepvalue=new Vector3(0,0,0);
	float MaxDim=0;
	GameObject instance;
	GameObject h;
	float pheight;
	float cheight;
	public string text;
	public void Star(string str)
	{



	

		text = str;
			string[] words = text.Split (' ');


			switch(words[1]) {

			case "on":
				
				if (GameObject.Find (words [2])) {
					
					instance = Instantiate (Resources.Load (words [0], typeof(GameObject))) as GameObject;
					instance.transform.GetChild (0).name = words [0];
					h = GameObject.Find (words [0]);
					cheight = h.GetComponent<Renderer> ().bounds.size.y;
					instance.transform.position = new Vector3 (0, pheight + cheight / 2, 0);
					Stepvalue = new Vector3 (2, 0, 0);
					instance.transform.position = instance.transform.position + Stepvalue;


				} else {
					
					instance = Instantiate (Resources.Load (words [2], typeof(GameObject))) as GameObject;
					instance.transform.GetChild (0).name = words [2];
					h = GameObject.Find (words [2]);
					pheight = h.GetComponent<Renderer> ().bounds.size.y;
					instance.transform.position = new Vector3 (0, pheight / 2, 0);
					instance.transform.position = instance.transform.position + Stepvalue;



					instance = Instantiate (Resources.Load (words [0], typeof(GameObject))) as GameObject;
					instance.transform.GetChild (0).name = words [0];
					h = GameObject.Find (words [0]);
					cheight = h.GetComponent<Renderer> ().bounds.size.y;
					instance.transform.position = new Vector3 (0, pheight + cheight / 2, 0);
					instance.transform.position = instance.transform.position + Stepvalue;

				}
				break;
			case "under"  :
				
							instance = Instantiate(Resources.Load(words[0], typeof(GameObject))) as GameObject;
							instance.transform.GetChild(0).name=words[0];
							h = GameObject.Find(words[0]);
							pheight = h.GetComponent<Renderer> ().bounds.size.y;
							instance.transform.position = new Vector3(0,pheight/2 ,0);




							instance = Instantiate(Resources.Load(words[2], typeof(GameObject))) as GameObject;
							instance.transform.GetChild(0).name=words[2];
							h = GameObject.Find(words[0]);
							cheight = h.GetComponent<Renderer> ().bounds.size.y;
							instance.transform.position = new Vector3(0,pheight+cheight/2,0);
							break;

			case "right":
					
				instance = Instantiate (Resources.Load (words [0], typeof(GameObject))) as GameObject;
				instance.transform.GetChild (0).name = words [0];
				h = GameObject.Find (words [0]);
				float pwidth = h.GetComponent<Renderer> ().bounds.size.x;
				pheight = h.GetComponent<Renderer> ().bounds.size.y;
				instance.transform.position = new Vector3 (0, pheight / 2, 0);

				instance = Instantiate (Resources.Load (words [2], typeof(GameObject))) as GameObject;
				instance.transform.GetChild (0).name = words [2];
				h = GameObject.Find (words [2]);
				float cwidth = h.GetComponent<Renderer> ().bounds.size.x;
				pheight = h.GetComponent<Renderer> ().bounds.size.y;
				instance.transform.position = new Vector3 ((cwidth / 2 + pwidth / 2) + 2, pheight / 2, 0);
				break;

			case "left":

				instance = Instantiate (Resources.Load (words [2], typeof(GameObject))) as GameObject;
				instance.transform.GetChild (0).name = words [2];
				h = GameObject.Find (words [2]);
				pwidth = h.GetComponent<Renderer> ().bounds.size.x;
				pheight = h.GetComponent<Renderer> ().bounds.size.y;
				instance.transform.position = new Vector3 (0,pheight/2, 0);

				instance = Instantiate (Resources.Load (words [0], typeof(GameObject))) as GameObject;
				instance.transform.GetChild (0).name = words [0];
				h = GameObject.Find (words [0]);
				cwidth = h.GetComponent<Renderer> ().bounds.size.x;
				pheight = h.GetComponent<Renderer> ().bounds.size.y;
				instance.transform.position = new Vector3 ((cwidth/2+pwidth/2)+2,pheight/2, 0);
				break;
				/*
			case "between":

				instance = Instantiate (Resources.Load (words [0], typeof(GameObject))) as GameObject;
				instance.transform.GetChild (0).name = words [0];
				h = GameObject.Find (words [0]);
				pwidth = h.GetComponent<Renderer> ().bounds.size.x;
				pheight = h.GetComponent<Renderer> ().bounds.size.y;
				instance.transform.position = new Vector3 (0, pheight / 2, 0);

				instance = Instantiate (Resources.Load (words [2], typeof(GameObject))) as GameObject;
				instance.transform.GetChild (0).name = words [2];
				h = GameObject.Find (words [2]);
				cwidth = h.GetComponent<Renderer> ().bounds.size.x;
				pheight = h.GetComponent<Renderer> ().bounds.size.y;
				instance.transform.position = new Vector3 ((cwidth / 2 + pwidth / 2) + 2, pheight / 2, 0);
				break;

				instance = Instantiate (Resources.Load (words [3], typeof(GameObject))) as GameObject;
				instance.transform.GetChild (0).name = words [3];
				h = GameObject.Find (words [3]);
				cwidth = h.GetComponent<Renderer> ().bounds.size.x;
				pheight = h.GetComponent<Renderer> ().bounds.size.y;
				instance.transform.position = new Vector3 (-(cwidth / 2 + pwidth / 2) + 2, pheight / 2, 0);
				break;
		
		*/

				
			}




			Stepvalue = Stepvalue +  new Vector3(0, 0, 3);



	
}


}
