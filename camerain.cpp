#include <opencv2/opencv.hpp>
#include <sys/time.h>
#include <fstream>
#include <sstream>
#include <string>


#include "stdio.h"
#include <iostream> 
#include <time.h>
using namespace cv;
using namespace std;



int main()
{    
	int i;
    	Mat src;
    	VideoCapture *cap = new VideoCapture(0);
    	if (!cap->isOpened()){
		return -1;
	}
    	

    	char str[100];
    	static struct timeval last_time;
    	struct timeval current_time;
    	static float last_fps;
    	float t;
    	float fps;
    	string x;
        string path;
   
    	ifstream file;
	    file.open("count.txt");
	    getline(file,x);
	    file.close();
	    

    	namedWindow("camera");
    


    	while (1) {
		if(!cap->read(src))
			return -1;
        	
		cout<<"img_save";
        

        	gettimeofday(&current_time, NULL);
        	t = (current_time.tv_sec - last_time.tv_sec)
                		+ (current_time.tv_usec - last_time.tv_usec) / 1000000.;
        	fps = 1. / t;
        	fps = last_fps * 0.8 + fps * 0.2;
        	last_fps = fps;
        	last_time = current_time;
        	sprintf(str, "%2.2f, %2.6f", fps, t);
        	putText(src, str, Point(20, 40), FONT_HERSHEY_DUPLEX, 1,
                	Scalar(0, 255, 0));

        	imshow("camera", src);

        	//-- bail out if escape was pressed
        	int c = waitKey(10);
        	if ((char) c == 27) {
            		break;
        	}
	
		else if ((char) c == 115) {
                        
			
			
			
            		imwrite("saved_image"+x+".jpg",src);
	    		stringstream obj;
	    		obj<<x;
	    		obj>>i;
			ofstream file("path.txt");
   			path ="saved_image"+x+".jpg";
			file<<path;
			file.close();
	    
	    		i=i+1;
	    		ofstream fout;
	    		fout.open("count.txt");
	    		fout<<i;
	    
	    		break;
	    
	    
        	}
    	}
    	delete cap;
    	destroyAllWindows();
	
    	return 0;
}



