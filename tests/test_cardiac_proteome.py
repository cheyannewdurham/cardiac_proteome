#!/usr/bin/env python

"""Tests for `cardiac_proteome` package."""

import pytest


from cardiac_proteome import cardiac_proteome

#import sys
import pytest
#import os
#import pandas as pd
from tempfile import TemporaryDirectory

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from combine_tsv_make_csv import combine_tsv_make_csv  



@pytest.fixture
def mock_tsv_files():
    with TemporaryDirectory() as temp_dir:
        file_1 = os.path.join(temp_dir, 'file1_target_psms.tsv')
        file_2 = os.path.join(temp_dir, 'file2_target_psms.tsv')

        data1 = "A\tB\tC\n1\t2\t3\n4\t5\t6\n"
        with open(file_1, 'w') as f1:
            f1.write(data1)

        data2 = "A\tB\tC\n7\t8\t9\n10\t11\t12\n"
        with open(file_2, 'w') as f2:
            f2.write(data2)

        yield temp_dir, file_1, file_2


@pytest.fixture
def expected_combined_df(mock_tsv_files):
    temp_dir, file_1, file_2 = mock_tsv_files
    expected_data = {
        "A": [1, 4, 7, 10],
        "B": [2, 5, 8, 11],
        "C": [3, 6, 9, 12],
    }
    return pd.DataFrame(expected_data)

def test_combine_tsv_make_csv(mock_tsv_files, expected_combined_df):
    temp_dir, file_1, file_2 = mock_tsv_files
    output_csv = os.path.join(temp_dir, 'combined_output.csv')

    combine_tsv_make_csv(temp_dir, output_csv)

    assert os.path.exists(output_csv), f"Expected CSV file at {output_csv} was not created"

    result_df = pd.read_csv(output_csv)

    pd.testing.assert_frame_equal(result_df, expected_combined_df)
