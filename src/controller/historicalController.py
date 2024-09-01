from datetime import datetime,timedelta

from waybackpy import WaybackMachineCDXServerAPI
import  requests

class HistorialSearch:
    def __init__(self, url, user_agent):
        self.url = url
        self.user_agent = user_agent

    def search_snapshot(self, year_ago=2, filename="snapshot.html"):
        """Busca y guarda una captura de pantalla de hace 'year_ago' años."""
        target_date = datetime.now() - timedelta(days=365 * year_ago)
        year, month_data, day = target_date.year, target_date.month, target_date.day
        cdx_api = WaybackMachineCDXServerAPI(self.url, self.user_agent)
        snapshot = cdx_api.near(year=year, month=month_data, day=day)
        if snapshot:
            print(f"Fecha: {snapshot.timestamp}, URL: {snapshot.archive_url}")
            self.download_snapshot(snapshot.archive_url, filename)
        else:
            print("No se encontró ninguna captura")

    @staticmethod
    def download_snapshot(archive_url, filename):
        """Descarga y guarda una captura de pantalla."""
        response = requests.get(archive_url)
        if response.status_code == 200:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f"Documento guardado exitosamente en el archivo {filename}")
        else:
            print(f"Error al descargar el archivo: {response.status_code}")

    def search_snapshots_by_extensions(self, year_ago=2, days_interval=30, extensiones=None, match_type="domain"):
        """Busca capturas de pantalla por extensiones de archivo."""
        if extensiones is None:
            extensiones = ["pdf", "doc", "docx", "ppt", "xls", "xlsx", "txt"]
        today = datetime.now()
        start_period = (today - timedelta(days=365 * year_ago)).strftime('%Y%m%d')
        end_period = (today - timedelta(days=(365 * year_ago) - days_interval)).strftime('%Y%m%d')
        cdx_api = WaybackMachineCDXServerAPI(
            url=self.url,
            user_agent=self.user_agent,
            start_timestamp=start_period,
            end_timestamp=end_period,
            match_type=match_type
        )

        regex_filter = "(" + "|".join([f".*\\.{ext}$" for ext in extensiones]) + ")"
        cdx_api.filters = [f"urlkey:{regex_filter}"]
        snapshots = cdx_api.snapshots()
        for snapshot in snapshots:
            print(f"Fecha: {snapshot.timestamp}, URL: {snapshot.archive_url}")