#!/bin/bash
cmd="./ch3_ex04_areacalculator.py"

function test_execution() {
    EXPECTED="$1" ; shift
    MISSING="$1" ; shift
    ARGUMENTS="$@"

    output="$($cmd $ARGUMENTS 2>&1)"
    echo "----------------------------------------------------------------"
    echo "Running command: $cmd $ARGUMENTS"
    echo "Program output:"
    sed -re 's/^/    /g' <<< "$output"
    if egrep -q "$EXPECTED" <<< "$output" ; then
        if egrep -q "$MISSING" <<< "$output" ; then
            echo "Expected to NOT find $MISSING but it's present in the output."
            echo "Result: NOT WORKING."
        else
            echo "Result: WORKING"
        fi
    else
        echo "Expected to find $EXPECTED in the output but couldn't find it."
        echo "Result: NOT WORKING."
    fi
    echo ""
}

# Test with no argument
test_execution ERROR "@" ''

# Test for a shape that doesn't exist
test_execution ERROR "@" bogus

##  Test triangles  ##

# Test for too few arguments
test_execution ERROR "@" triangle
test_execution ERROR "@" triangle 3
test_execution ERROR "@" triangle 3.2
# Test for invalid arguments
test_execution ERROR "@" triangle -3.2 -5.4
# Test for correct data
test_execution 7.5   ERROR triangle 3 5
test_execution 8.64  ERROR triangle 3.2 5.4
# Test for additional arguments
test_execution 7.5   ERROR triangle 3 5 4

##  Test circles  ##

# Test for too few arguments
test_execution ERROR "@" circle
# Test for invalid arguments
test_execution ERROR "@" circle -4.3
# Test for correct data
test_execution 12.56 ERROR circle 4
test_execution 13.50 ERROR circle 4.3
# Test for additional arguments
test_execution 12.56 ERROR circle 4 5
