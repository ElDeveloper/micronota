# ----------------------------------------------------------------------------
# Copyright (c) 2015--, micronota development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

import click


@click.command()
@click.option('-i', '--input_fp', type=click.File('r'),
              required=True,
              help='Input file path.')
@click.option('-o', '--output_fp', type=click.File('w'),
              required=True,
              help='Output file path.')
@click.pass_context
def cli(ctx, input_fp, output_fp):
    '''Format conversion.'''
    pass
