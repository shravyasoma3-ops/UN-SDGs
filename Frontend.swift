import MapKit
import SwiftUI

@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}


struct ContentView: View {
    @State private var position: MapCameraPosition = .region( MKCoordinateRegion(
        center: CLLocationCoordinate2D(latitude:12.9716, longitude:77.5946), span:  MKCoordinateSpan(latitudeDelta: 0.5, longitudeDelta:0.5)
    )
    )
    struct Forest: Identifiable {
        let id = UUID()
        let district: String
        let taluk: String
        let village: String
        let syno: String
        let coordinate: CLLocationCoordinate2D
        let radiusinMeters: Double
        let hasWildlife: Bool
        let areaInSquareMeters: Double

        var areaInSquareMeters: Double {
            return Double.pi * radiusinMeters * radiusinMeters
    }
    @State var text: String = "";
    
    @State private var forests: [Forest] = [
        Forest(
            district: "Bagalkot",
            taluk: "Bagalkot",
            village: "Mugalolli",
            syno: "37/1A",
            coordinate: CLLocationCoordinate2D(latitude: 16.1850, longitude: 75.6962), 
            areaInSquareMeters: 10500,
            hasWildlife: true
        ),
        Forest(
            district: "Bagalkot",
            taluk: "Bagalkot",
            village: "Chikkahodular",
            syno: "46",
            coordinate: CLLocationCoordinate2D(latitude:16.3333, longitude: 75.8667 ), 
            areaInSquareMeters: 259000,
            hasWildlife: true
        ),
        Forest(
            district: "Bagalkot",
            taluk: "Hungund",
            village: "Kamatagi",
            syno: "101",
            coordinate: CLLocationCoordinate2D(latitude: 16.0167, longitude: 75.7167), 
            areaInSquareMeters: 125000,
            hasWildlife: true
        ),
        Forest(
            district: "Bagalkot",
            taluk: "Bagalkot",
            village: "Mugalolli",
            syno: "25/1A",
            coordinate: CLLocationCoordinate2D(latitude: 16.1850, longitude: 75.6962), 
            areaInSquareMeters: 728700,
            hasWildlife: true
        ),
        Forest(
            district: "Bagalkot",
            taluk: "Bagalkot",
            village: "Mudapaljivi",
            syno: "3/1A",
            coordinate: CLLocationCoordinate2D(latitude: 6.2350, longitude: 75.8077), 
            areaInSquareMeters: 404600,
            hasWildlife: true
        ),
        Forest(
            district: "Bagalkot",
            taluk: "Bagalkot",
            village: "Rampur",
            syno: "26/32",
            coordinate: CLLocationCoordinate2D(latitude: 16.2833, longitude: 75.8667), 
            areaInSquareMeters: 1651200,
            hasWildlife: true
        ),
        Forest(
            district: "Belgavi",
            taluk: "Athani",
            village: "Athani",
            syno: "963",
            coordinate: CLLocationCoordinate2D(latitude:16.7241, longitude: 75.0638), 
            areaInSquareMeters: 3930000,
            hasWildlife: true
        ),
        Forest(
            district: "Belgavi",
            taluk: "Athani",
            village: "Athani",
            syno: "1220",
            coordinate: CLLocationCoordinate2D(latitude: 16.7241, longitude: 75.0638), 
            areaInSquareMeters: 60900,
            hasWildlife: true
        ),
        Forest(
            district: "Belgavi",
            taluk: "Athani",
            village: "Athani",
            syno: "1228",
            coordinate: CLLocationCoordinate2D(latitude: 16.7241, longitude: 75.0638), 
            areaInSquareMeters: 69200,
            hasWildlife: true
        ),
        Forest(
            district: "Belgavi",
            taluk: "Athani",
            village: "Athani",
            syno: "1240",
            coordinate: CLLocationCoordinate2D(latitude: 16.7241, longitude: 75.0638), 
            areaInSquareMeters: 97600,
            hasWildlife: true
        ),
        Forest(
            district: "Belgavi",
            taluk: "Athani",
            village: "Athani",
            syno: "1386",
            coordinate: CLLocationCoordinate2D(latitude: 16.7241, longitude: 75.0638), 
            areaInSquareMeters: 178500,
            hasWildlife: true
        ),
        Forest(
            district: "Belgavi",
            taluk: "Athani",
            village: "Athani",
            syno: "1008/A",
            coordinate: CLLocationCoordinate2D(latitude: 6.7241°, longitude: 75.0638), 
            areaInSquareMeters: 90300,
            hasWildlife: true
        ),
        Forest(
            district: "Belgavi",
            taluk: "Athani",
            village: "Darur",
            syno: "16",
            coordinate: CLLocationCoordinate2D(latitude: 6.7200°, longitude: 75.0600), 
            areaInSquareMeters: 36400,
            hasWildlife: true
        ),
        Forest(
            district: "Belgavi",
            taluk: "Athani",
            village: "Darur",
            syno: "18",
            coordinate: CLLocationCoordinate2D(latitude: 16.7200, longitude: 75.0600), 
            areaInSquareMeters: 90000,
            hasWildlife: true
        ),
        Forest(
            district: "Belgavi",
            taluk: "Athani",
            village: "Satti",
            syno: "526",
            coordinate: CLLocationCoordinate2D(latitude: 16.7200, longitude: 75.0600), 
            areaInSquareMeters: 211300,
            hasWildlife: true
        ),
        Forest(
            district: "Belgavi",
            taluk: "Athani",
            village: "Satti",
            syno: "667",
            coordinate: CLLocationCoordinate2D(latitude: 16.7200, longitude:  75.0600), 
            areaInSquareMeters: 405100,
            hasWildlife: true
        ),
        Forest(
            district: "Belgavi",
            taluk: "Belgavi",
            village: "Dhamme",
            syno: "11/A",
            coordinate: CLLocationCoordinate2D(latitude: 15.8833, longitude: 74.5167), 
            areaInSquareMeters: 6500,
            hasWildlife: false
        ),
        Forest(
            district: "Belgavi",
            taluk: "Belgavi",
            village: "Dhame",
            syno: "16/2 A",
            coordinate: CLLocationCoordinate2D(latitude: 15.8833, longitude: 74.516), 
            areaInSquareMeters: 3000,
            hasWildlife: false
        ),
        Forest(
            district: "Belgavi",
            taluk: "Belgavi",
            village: "Dhame",
            syno: "20/2 A",
            coordinate: CLLocationCoordinate2D(latitude: 15.8833, longitude: 74.5167), 
            areaInSquareMeters: 5200,
            hasWildlife: false
                )
    ]
    var body: some View {
        ZStack(alignment: .bottom){
        }
        Map(position: $position) {
            ForEach(forests) {forest in
                MapCircle(center: forest.coordinate, radius: forest.radiusinMeters)
                    .foregroundStyle(.green.opacity(0.20))
                    .stroke(.green, lineWidth: 2.3)
                Annotation(forest.village, coordinate: forest.coordinate) {
                    Menu {
                        Text(forest.village)
                            .font(.headline) 
                        if forest.hasWildlife {
                            Text("Animals live here!")
                                .font(.headline)
                        }
                        else { 
                            Text("No animals live here!")
                                .font(.headline)
                        }
                    }
                    label: {
                        Image(systemName: "tree.fill")
                            .padding(8)
                            .background(Color.green)
                            .foregroundColor(.white)
                            .clipShape(Circle())
                    }
                }
            }
        }
        HStack {
            TextField("Enter your location", text: self.$text)
                .textFieldStyle(RoundedBorderTextFieldStyle())
            Button("Go", action: {
                searchLocation(query: text)
            })
            .padding()
            .background(.thinMaterial)
        }
    }
    
    func searchLocation(query: String){
        let request = MKLocalSearch.Request()
        request.naturalLanguageQuery = query 
        let search = MKLocalSearch(request: request)
        
        search.start { response, error in
            guard let response = response, let item = response.mapItems.first else { 
                return
            }
            let coordinate = item.location.coordinate
            
            withAnimation {
                position = .region(
                    MKCoordinateRegion(
                        center: coordinate, span: MKCoordinateSpan(latitudeDelta: 0.05, longitudeDelta: 0.05))
                )
            }
        }
    }
}
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
        
    }
}
