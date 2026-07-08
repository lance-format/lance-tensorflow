# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright The Lance Authors

from importlib.metadata import version


def test_package_is_installed():
    assert version("lance-tensorflow")
