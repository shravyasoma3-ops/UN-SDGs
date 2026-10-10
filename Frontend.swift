import MapKit
import SwiftUI

struct ContentView: View {
    @State private var position: MapCameraPosition = .region( MKCoordinateRegion(
        center: CLLocationCoordinate2D(latitude:12.9716, longitude:77.5946), span:  MKCoordinateSpan(latitudeDelta: 0.5, longitudeDelta:0.5)
    )
    )
    @State var text: String = "";
    var body: some View {
        Map(position: $position)
        HStack {
            TextField("Enter your location", text: self.$text)
                .textFieldStyle(RoundedBorderTextFieldStyle())
            Button("Go", action: {
                searchLocation(query: text)
            })
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
    
    struct ContentView_Previews: PreviewProvider {
        static var previews: some View {
            ContentView()
        }
    }
}
