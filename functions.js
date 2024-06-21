function station_bereken(km_naar_station, kilometer_per_liter, hoeveelheid_brandstof) {
    var afstand_aflegbaar = kilometer_per_liter * hoeveelheid_brandstof;
    if (afstand_aflegbaar >= km_naar_station) {
        return true;
    } else {
        return false;
    }
}

console.log(station_bereken(80, 10, 8));
console.log(station_bereken(100, 10, 8));
console.log(station_bereken(8, 10, 8));
console.log(station_bereken(10, 10, 10));
console.log(station_bereken(7, 3, 7));
console.log(station_bereken(60, 5, 4));