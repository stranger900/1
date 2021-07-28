import pytest, sys

def main():
    print('Extracted arg2 is => %s' % sys.argv[2])
    print('Extracted arg3 is => %s' % sys.argv[3])
    pytest.main([sys.argv[1]])

if __name__ == '__main__':
    main()
