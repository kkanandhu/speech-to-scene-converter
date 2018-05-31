using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class test : MonoBehaviour {
    double x1=0, x2=6, x3, y1=0, y2=0, y3, mx, my, nx, ny;
    
    
	// Use this for initialization
	void Start () {
        mx = (x1 + x2) / 2;
        my = (y1 + y2) / 2;
        nx = 0.8660254 * (y1 - y2);
        ny = 0.8660254 * (x2 - x1);
        x3 = mx + nx;
        y3 = nx + ny;
        Debug.Log("x3="+x3+"y3="+y3);
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}
}
