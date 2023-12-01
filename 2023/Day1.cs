using System;
using System.IO;

public class Day1 : IDay
{
    public void Run() {
        string inputPath = "input/Day1.txt";
        try {
            int sum = 0;
            // Read each line of the file
            foreach (string line in File.ReadLines(inputPath)) {
                sum += ProcessLine(line);
            }
            Console.WriteLine($"Sum of calibration values: {sum}");
        }
        catch (IOException e) {
            Console.WriteLine($"An error occurred while reading the file: {e.Message}");
        }
    }

    int ProcessLine(string line) {
        string firstDigit, lastDigit = "";
        for (int i=0; i< a.line; i++) {
            if (Char.IsDigit(a[i])) {
                b += a[i];
            }
        }
        // Find first digit

        // Find last digit

        // Concat
    }
}
