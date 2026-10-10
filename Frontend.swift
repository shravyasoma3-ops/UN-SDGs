import MapKit
import SwiftUI

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
    }
    @State var text: String = "";
    
    @State private var forests: [Forest] = [
        Forest(
            district: "Bengaluru Urban",
            taluk: "Uttarahalli",
            village: "Turahalli village",
            syno: "5",
            coordinate: CLLocationCoordinate2D(latitude: 12.882, longitude: 77.525), 
            radiusinMeters: 872,
            hasWildlife: true
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
