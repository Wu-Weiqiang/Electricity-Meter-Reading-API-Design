class ElectricityAccount:
    def __init__(self, meter_id, area, region, dwelling_type):
        self.meter_id = meter_id
        self.area = area
        self.region = region
        self.dwelling_type = dwelling_type

    def __str__(self):
        return (
            f"Meter Id: {self.meter_id}\n"
            f"Area: {self.area}\n"
            f"Region: {self.region}\n"
            f"Dwelling Type: {self.dwelling_type}\n"
        )

    def to_dict(self):
        """Convert the ElectricityAccount object to a dictionary"""
        return {
            'meter_id': self.meter_id,
            'area': self.area,
            'region': self.region,
            'dwelling_type': self.dwelling_type
        }

    @classmethod
    def from_dict(cls, data):
        """Create an ElectricityAccount instance from a dictionary"""
        return cls(
            meter_id=data.get('meter_id'),
            area=data.get('area'),
            region=data.get('region'),
            dwelling_type=data.get('dwelling_type')
        )
