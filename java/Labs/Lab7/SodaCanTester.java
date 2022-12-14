
/**
 * A class to calculate the area of several SodaCans
 */
public class SodaCanTester {
   /**
    * Calculates the average area in an array list of SodaCans
    * 
    * @param SodaCanArray the SodaCans
    * @return the average area of SodaCanArray
    */

   private static double averageArea(Measurable[] sodaCanArray) {
      // -----------Start below here. To do: approximate lines of code = 4
      // get the measure of area from all sodaCan objects in the array, add them up
      // and
      // compute the average. return the average

      if (sodaCanArray.length == 0) {
         return 0.0;
      }

      double sum = 0;

      for (Measurable m : sodaCanArray) {
         sum += m.getMeasure();
      }

      return sum / sodaCanArray.length;

      // -----------------End here. Please do not remove this comment. Reminder: no
      // changes outside the todo regions.
   }

   public static void main(String[] args) {
      SodaCan[] sodaCans = new SodaCan[4];
      sodaCans[0] = new SodaCan(2, 3);
      sodaCans[1] = new SodaCan(3, 3);
      sodaCans[2] = new SodaCan(5, 7);
      sodaCans[3] = new SodaCan(1, 1);
      System.out.printf("The average area is: %10.2f", averageArea(sodaCans));
      System.out.println("\nExpected:\nThe average area is:     186.92");
   }
}
