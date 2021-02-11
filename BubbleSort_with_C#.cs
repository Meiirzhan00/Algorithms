            int[] numbers = new int[7];
            Console.WriteLine("Input is seven number !");
            for (int i = 0; i < numbers.Length; i++)
            {
                Console.Write("{0} number : ", i + 1);
                numbers[i] = Int32.Parse(Console.ReadLine());
            }

            foreach (int m in numbers)
                Console.Write($" {m} ");

            int temp;

            for (int j = 0; j < numbers.Length - 1; j++)
            {
                for (int k = j + 1; k < numbers.Length; k++)
                {
                    if (numbers[j] > numbers[k])
                    {
                        temp = numbers[j];
                        numbers[j] = numbers[k];
                        numbers[k] = temp;

                    }
                }
            }

            Console.WriteLine();

            foreach (int l in numbers)
                Console.Write($" {l} ");
