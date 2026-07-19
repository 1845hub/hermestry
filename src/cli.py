import argparse
from agent.core import Agent
from agent.planner import Planner
from agent.executor import Executor


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cli', action='store_true', help='interactive CLI')
    args = parser.parse_args()

    planner = Planner()
    executor = Executor()
    agent = Agent(planner, executor)

    if args.cli:
        print('Hermestry CLI. type "quit" to exit.')
        while True:
            t = input('> ')
            if t.strip() in ('quit','exit'):
                break
            resp = agent.receive(t)
            print(resp)

if __name__ == '__main__':
    main()
