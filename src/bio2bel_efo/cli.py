# -*- coding: utf-8 -*-

"""Run this script with either :code:`python3 -m bio2bel_efo arty`"""

from __future__ import print_function

import logging
import sys

import click

from pybel_tools.ols_utils import OlsNamespaceOntology
from .run import MODULE_DOMAIN, MODULE_ENCODING, MODULE_NAME


@click.group()
def main():
    """Experimental Factor Ontology to BEL"""
    logging.basicConfig(level=10, format="%(asctime)s - %(levelname)s - %(message)s")


@main.command()
@click.option('-b', '--ols-base', help="Custom OLS base url")
@click.option('-o', '--output', type=click.File('w'), default=sys.stdout)
def write(ols_base, output):
    """Writes BEL namespace"""
    ontology = OlsNamespaceOntology(MODULE_NAME, MODULE_DOMAIN, encoding=MODULE_ENCODING, ols_base=ols_base)
    ontology.write_namespace(output)


@main.command()
@click.option('-b', '--ols-base', help="Custom OLS base url")
@click.option('--no-hash-check', is_flag=True)
def deploy(ols_base=None, no_hash_check=False):
    """Deploy to Artifactory"""
    ontology = OlsNamespaceOntology(MODULE_NAME, MODULE_DOMAIN, encoding=MODULE_ENCODING, ols_base=ols_base)
    success = ontology.deploy_namespace(hash_check=(not no_hash_check))
    click.echo('Deployed to {}'.format(success) if success else 'Duplicate not deployed')


if __name__ == '__main__':
    main()
