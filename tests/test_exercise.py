import pytest
import src.exercise

def test_exercise():
    input_values = ["5","25","-2","135"]
    input_values_stored = ["5","25","-2","135"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert [output[0],output[1],output[2],output[3]] == ["How old are you?","OK","How old are you?","OK"]
    assert [output[4],output[5],output[6],output[7]] == ["How old are you?","Impossible!","How old are you?","Impossible!"]
