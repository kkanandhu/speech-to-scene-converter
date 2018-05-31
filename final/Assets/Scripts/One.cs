using UnityEngine;
using System.Collections;
using System.IO;
using UnityEngine.UI;
public class One : MonoBehaviour {
	public Two t;

	public InputField field;
	public string context="";
	public string uttarance="";
	public SpeechTotext sp;
	public Prepo pr;
	public Generate gr;
	public Relation rl;
	public Color cr;
	public void prepo(string mystr)
	{
		pr.x = mystr;
		pr.Star ();
		gr.gen ();
		rl.relate();
		cr.color ();
	}


	public void speech()
	{
		sp.callpy ();
		//Debug.Log(sp.myString);
		field.text =sp.myString;
	}



	// Use this for initialization
	public void getcoref () {

		if (context == "") {

			context = field.text;
			uttarance = field.text;
			t.x = context;
			t.y = uttarance;
			//Debug.Log ("con : "+context);
			//Debug.Log ("utt  : "+uttarance);
			t.Star ();
			//Debug.Log (t.myString);
			context = t.myString;

		} else {
			uttarance=field.text;
			t.x = context;
			t.y = uttarance;
			//Debug.Log ("con : "+context);
			//Debug.Log ("utt  : "+uttarance);
			t.Star ();
			context = t.myString;
		}


	







		prepo (t.myString);

	}

	public void clear()
	{
		
		string g = "bird penta table box ";
		string[] lists = g.Split (' ');
		string tar;

		foreach (string target in lists) {
			tar= target + "(Clone)";
			GameObject.Destroy(GameObject.Find (tar));
		}


	}

}
