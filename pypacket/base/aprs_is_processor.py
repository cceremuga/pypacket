from pypacket.base.processor import ProcessorBase


class AprsIsProcessor(ProcessorBase):
    def load(self, config, log_handler, decoder_subprocess):
        log_handler.log_info('Starting processor subprocess.')
        log_handler.log_info('Processor attaching to decoder.')
