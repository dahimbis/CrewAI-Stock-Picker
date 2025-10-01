#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from stock_picker.crew import StockPicker

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
        Run the Research Crew
    """

    inputs = {
        "sector":"Technology",
        "current_date": str(datetime.now())
    }

    result = StockPicker().crew().kickoff(inputs=inputs)

    print("\n\n==FINAL DECISION==\n\n")
    print(result.raw)



if __name__ == "__main__":
    run()
   