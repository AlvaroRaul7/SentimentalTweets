/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package preprocesamientotweets;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;


/**
 *
 * @author alvaro-pc
 */
public class PreprocesamientoTweets {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws FileNotFoundException, IOException {
        // TODO code application logic here
     
        depurarCSViess();
        depurarCSVsri();
        depurarCSVcpccs();
        
       
    }
    
       public static String depurarlinea(String linea){
           linea=linea.replace("@", "");
           linea=linea.replace("RT","");
           linea=linea.replace("/", "");
           linea=linea.replace("http", "");
           linea=linea.replace(":","");
           linea=linea.replace("#","");
           linea= linea.replace("%", "");
           linea=linea.replace("$","");
           linea=linea.replace("&","");
           linea=linea.replace("*","");
           return linea;
       }
       
       
       public static void depurarCSViess() throws FileNotFoundException, IOException{
            String rutacsv ="tweets#IESS.csv";
            BufferedReader csvReader = new BufferedReader(new FileReader(rutacsv));
            FileWriter csvWriter = new FileWriter("tweetsdepuradosIESS.csv");
            String row;
             while ((row = csvReader.readLine()) != null) {
                String[] linearchivo = row.split(",");
                System.out.println(linearchivo[1]+" "+linearchivo[2]);
                String lineadepurada = depurarlinea(linearchivo[2]);
                linearchivo[2]=lineadepurada;
                csvWriter.append(String.join(",", linearchivo));
                csvWriter.append("\n");
                
           }
        csvReader.close();
        csvWriter.close();
       }
       
       public static void depurarCSVsri() throws FileNotFoundException, IOException{
            String rutacsv ="tweets#SRI.csv";
            BufferedReader csvReader = new BufferedReader(new FileReader(rutacsv));
            FileWriter csvWriter = new FileWriter("tweetsdepuradossri.csv");
            String row;
             while ((row = csvReader.readLine()) != null) {
                String[] linearchivo = row.split(",");
                System.out.println(linearchivo[1]+" "+linearchivo[2]);
                String lineadepurada = depurarlinea(linearchivo[2]);
                linearchivo[2]=lineadepurada;
                csvWriter.append(String.join(",", linearchivo));
                csvWriter.append("\n");
                
           }
        csvReader.close();
        csvWriter.close();
       }
       
         public static void depurarCSVcpccs() throws FileNotFoundException, IOException{
            String rutacsv ="tweets#CPCCS.csv";
            BufferedReader csvReader = new BufferedReader(new FileReader(rutacsv));
            FileWriter csvWriter = new FileWriter("tweetsdepuradoscpccs.csv");
            String row;
             while ((row = csvReader.readLine()) != null) {
                String[] linearchivo = row.split(",");
                System.out.println(linearchivo[1]+" "+linearchivo[2]);
                String lineadepurada = depurarlinea(linearchivo[2]);
                linearchivo[2]=lineadepurada;
                csvWriter.append(String.join(",", linearchivo));
                csvWriter.append("\n");
                
           }
        csvReader.close();
        csvWriter.close();
       }
    
}
