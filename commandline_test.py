import subprocess


if __name__ == "__main__":
    """Test script voor het callen van een bash script vanuit python en het meegeven van parameters
    """
    s1 = "Hallo dit is een test"
    s2 = "Dit is een tweede string om te kijken hoe het gaat met meerdere parameters"
    subprocess.call(["sbatch commandline_test.sh", s1, s2])
