import re


class Validator:

    def __init__(self, values):
        self.status = values['status']
        self.build = values['build']
        self.hw_revision = values['hw_revision']
        self.carrier = values['carrier']
        self.sn = values['sn']
        self.sim = values['sim']
        self.sd = values['sd']
        self.hw_version = values['hw_version']

    def validate_status(self):
        return self.status == 'Review'

    def validate_primary_sw(self):
        builds_regex = '(^(P|Q|R|S|T))([A-Z]|[0-9])*[.]{1}([A-Z]|[0-9])*([-]?([A-Z]|[0-9]))*(_cid50)?'
        result = re.search(builds_regex, self.build)
        return result.group() == self.build if result is not None else False

    def validate_hw_revision(self):
        hws_regex = '((EVT.*){1})|((DVT.*){1})|((PVT.*){1})'
        result = re.search(hws_regex, self.hw_revision)
        return result.group() == self.hw_revision if result is not None else False

    def validate_carrier(self):
        carriers_regex = '^((Carrier)?).*(((amx)|(ret)|(open)){1}).*'
        result = re.search(carriers_regex, self.carrier, re.IGNORECASE)
        return result.group() == self.carrier if result is not None else False

    def validate_sn(self):
        sns_regex = '^((Serial){1}).*([A-Z]{1}).*([0-9]{1}).*'
        result = re.search(sns_regex, self.sn)
        return result.group() == self.sn if result is not None else False

    def validate_sim_card(self):
        sims_regex = '^((SIM(( )?)Card){1}).*(((TIM)|(Vivo)|(Claro)|(Oi)){1}).*'
        result = re.search(sims_regex, self.sim, re.IGNORECASE)
        return result.group() == self.sim if result is not None else False

    def validate_sd_card(self):
        sds_regex = '^((SD(( )?)Card){1}).*((GB){1}).*((class){1}).*'
        result = re.search(sds_regex, self.sd, re.IGNORECASE)
        return result.group() == self.sd if result is not None else False

    def validate_hw_version(self):
        hws_regex = '.*(((EVT.*){1})|((DVT.*){1})|((PVT.*){1}))'
        result = re.search(hws_regex, self.hw_version)
        return result.group() == self.hw_version if result is not None else False
