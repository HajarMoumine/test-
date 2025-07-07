from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class NewParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from test.parsers.parser import NewParser

        return NewParser(**self.model_dump())


class koalaExperimentParserEntryPoint(ParserEntryPoint):

    def load(self):
        from test.parsers.koala_batch_parser import koalaExperimentParser

        return koalaExperimentParser(**self.model_dump())


class koalaParserEntryPoint(ParserEntryPoint):

    def load(self):
        from test.parsers.koala_measurement_parser import koalaParser

        return koalaParser(**self.model_dump())


parser_entry_point = NewParserEntryPoint(
    name='NewParser',
    description='New parser entry point configuration.',
    mainfile_name_re=r'.*\.newmainfilename',
)


koala_experiment_parser_entry_point = koalaExperimentParserEntryPoint(
    name='koalaExperimentParserEntryPoint',
    description='koala experiment parser entry point configuration.',
    mainfile_name_re='^(.+\.xlsx)$',
    mainfile_mime_re='(application|text|image)/.*',
)


koala_parser_entry_point = koalaParserEntryPoint(
    name='koalaParserEntryPoint',
    description='koala parser entry point configuration.',
    mainfile_name_re='^.+\.?.+\.((eqe|jv|mppt)\..{1,4})$',
    mainfile_mime_re='(application|text|image)/.*',
)
