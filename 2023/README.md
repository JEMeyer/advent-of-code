# Advent of Code 2023 Solutions in .NET 8.0

This project contains my solutions for the [Advent of Code 2023](https://adventofcode.com/2023) challenges, implemented in C# using .NET 7.0. Each day's challenge is encapsulated in its own class, following a consistent interface for ease of execution and maintenance.

## Structure

- **IDay Interface**: A common interface `IDay` that each day's challenge implements. It contains a `Run` method, which is the entry point for each day's solution.
- **Day Classes**: Each day's solution is implemented in a separate class (e.g., `Day1`, `Day2`, etc.), all implementing the `IDay` interface.
- **Program.cs**: The main entry point of the application. It dynamically selects and runs the appropriate day's solution based on the command-line argument provided.

## Prerequisites

To run these solutions, you will need:

- [.NET 8.0 SDK](https://dotnet.microsoft.com/download/dotnet/8.0)

## Running a Solution

To run a solution for a specific day, use the command line to navigate to the project's root directory in the `/2023/` folder and then run the program with the day number as an argument. For example, to run the solution for Day 1, use:

```bash
dotnet run -- 1
```

Replace `1` with the desired day number to run a different day's solution.

## Implementation Details

- **Reflection**: The program uses reflection to dynamically instantiate the class corresponding to the day's challenge. This approach allows for adding new days without modifying the main program logic.
- **Error Handling**: Basic error handling is included to manage common issues, such as invalid input or missing implementations for a day.
- **Scalability**: The design is scalable, making it straightforward to add new days. Simply create a new class for the day and ensure it implements the `IDay` interface.

## Contributing

While this project is primarily for personal use as I work through the Advent of Code 2023 challenges, suggestions or improvements are welcome. Please feel free to open an issue or a pull request.

## License

This project is open-sourced under the MIT License, which can be found in the [parent directory](../LICENSE).
