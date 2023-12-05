using System.Text.RegularExpressions;

namespace AdventOfCode;

public class ColorProperties(int? red = null, int? green = null, int? blue = null)
{
    public int? Red { get; set; } = red;
    public int? Green { get; set; } = green;
    public int? Blue { get; set; } = blue;
}


public partial class Day2 : IDay
{

    public void Run() {
        ColorProperties Day2_1Limits = new(12, 13, 14);
        string inputPath = "input/Day1.txt";

        // We just need to check that each line doesn't have an invalid config. If valid, add to sum
        foreach (string line in File.ReadLines(inputPath)) {
            Regex regex = MyRegex();
            var matches = regex.Matches(line);

        }
    }

    bool IsValidLine(string line) {
        return true;
    }

    [GeneratedRegex(@"Game (\d+):\s(.+)")]
    private static partial Regex MyRegex();
}
