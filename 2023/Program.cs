using System.Reflection;
using AdventOfCode;

class Program
{
    static void Main(string[] args)
    {
        if (args.Length == 0 || !int.TryParse(args[0], out int dayNumber))
        {
            Console.WriteLine("Please specify a day number.");
            return;
        }

        string className = $"Day{dayNumber}";
        Type? dayType = Assembly.GetExecutingAssembly().GetTypes()
            .FirstOrDefault(t => t.Name.Equals(className, StringComparison.OrdinalIgnoreCase));

        if (dayType == null)
        {
            Console.WriteLine($"Day {dayNumber} is not implemented.");
            return;
        }

        if (Activator.CreateInstance(dayType) is IDay dayInstance)
        {
            dayInstance.Run();
        }
        else
        {
            Console.WriteLine($"Day {dayNumber} does not implement IDay interface.");
        }
    }
}
