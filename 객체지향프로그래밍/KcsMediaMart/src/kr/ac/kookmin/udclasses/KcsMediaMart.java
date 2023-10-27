package kr.ac.kookmin.udclasses;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;

public class KcsMediaMart {

	public static void main(String[] args) throws FileNotFoundException {
		Properties prop = new Properties();
		FileInputStream fis = new FileInputStream("media.properties");
		try {
			prop.load(fis);
		}
		catch(IOException e) {
		}
		DataInitializer data = new DataInitializer();
		Order anOrder = new Order();
			
		int dvdsToBeAdded = 3;
		for(int dvdNumber = 1; dvdNumber <= dvdsToBeAdded; dvdNumber++) {
			DVD dvd = data.retrieveDvd(prop, dvdNumber);
			anOrder.addDVD(dvd);
		}
		System.out.print("Total Cost is: ");
		System.out.println(anOrder.totalCost());	
	}
}
