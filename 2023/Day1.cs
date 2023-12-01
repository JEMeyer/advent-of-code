namespace AdventOfCode;

public class Day1 : IDay
{
    public void Run() {
        string inputPath = "input/Day1.txt";
        try {
            int p1Sum = 0, p2Sum = 0;
            // Read each line of the file
            foreach (string line in File.ReadLines(inputPath)) {
                p1Sum += Part1ProcessLine(line);
                p2Sum += Part2ProcessLine(line);
            }
            Console.WriteLine($"Part 1 sum of calibration values: {p1Sum}");
            Console.WriteLine($"Part 2 sum of calibration values: {p2Sum}");
        }
        catch (IOException e) {
            Console.WriteLine($"An error occurred while reading the file: {e.Message}");
        }
    }

    static int Part1ProcessLine(string line) {
        char? firstDigit = null, lastDigit = null;
        for (int i=0; i < line.Length; i++) {
            if (char.IsDigit(line[i])) {
                // Always update last
                lastDigit = line[i];

                // Only update first if it's unset
                firstDigit ??= line[i];
            }
        }
        // Concat + return
        return int.Parse(firstDigit.ToString() + lastDigit.ToString());
    }

    static readonly string[] numbersAsString = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

    static bool ParseCharDigitOrStringDigit(string input, out char number) {
        if (char.IsDigit(input[0])) {
            number = input[0];
            return true;
        }

        int index = -1;
        for (int i = 0; i < numbersAsString.Length; i++) {
            if (input.StartsWith(numbersAsString[i], StringComparison.CurrentCultureIgnoreCase)) {
                index = i;
                break;
            }
        }

        if (index != -1) {
            number = (index + 1).ToString()[0];
            return true;
        }

        number = '\0';
        return false;
    }

    static int Part2ProcessLine(string line) {
        char? firstDigit = null, lastDigit = null;
        for (int i=0; i < line.Length; i++) {
            if (ParseCharDigitOrStringDigit(line[i..], out char number)) {
                // Always update last
                lastDigit = number;

                // Only update first if it's unset
                firstDigit ??= number;
            }
        }
        // Concat + return
        return int.Parse(firstDigit.ToString() + lastDigit.ToString());
    }
}
