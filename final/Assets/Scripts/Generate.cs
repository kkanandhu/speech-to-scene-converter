using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System;
public class Generate : MonoBehaviour {

public  Prepo pr;
GameObject instance;
public test ts;
public void gen()
{
string[] pipe = pr.mySplit[0].Split(' ');
foreach (string item in pipe){
if(item!="."){
try
{


					string[] items=item.Split('.');
					int x = Int32.Parse(items[0]);
					float tolerance=0;
					//GENERATE SPACE
					string a=items[1]+(1).ToString();
					Vector2 pos;
					for(int i=0;i<x;i++)
					{
						
						string name=items[1]+(i+1).ToString();
					
						if (!GameObject.Find (name)) {


						instance = Instantiate (Resources.Load (items[1], typeof(GameObject))) as GameObject;
						instance.transform.GetChild (0).name = name;
						
						float height =GameObject.Find (name).GetComponent<Renderer> ().bounds.size.y;
							float width =GameObject.Find (name).GetComponent<Renderer> ().bounds.size.x;
							pos=ts.getpoint(i+1,width+width/5);
							Debug.Log(pos);
							GameObject.Find (name).transform.position=new Vector3(pos.x,height/2,pos.y);

					}
					else {



					}

					}
					//GENERATE SPACE





}
				catch(System.Exception e)
{

}

}
}
}
}
