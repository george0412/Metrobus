// Crea la instancia
let ns = {};

// Crea el model
ns.model = (function() {
    'use strict';
    let $event_pump = $('body');

    // Regresa el API
    return {
        'read': function() {
            let ajax_options = {
                type: 'GET',
                url: 'api/metrobus',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_read_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        }
    };
}());

// Crea la vista
ns.view = (function() {
    'use strict';

    let metrobus_id = $('#metrobus_id'),
        $update_time = $('#update_time');
        $vehicle_id = $('#vehicle_id');
        $geographic_point = $('#geographic_point');
        $position_longitude = $('#position_longitude');
        $position_latitude = $('#position_latitude');
        $alcaldia = $('#alcaldia');
        $vehicle_current_status = $('#vehicle_current_status');
        $position_speed = $('#position_speed');
        alert();
    // return the API
    return {
        reset: function() {
            $metrobus_id.val('');
            $update_time.val(''),
            $vehicle_id.val('').focus();
            $geographic_point.val('');
            $position_longitude.val('');
            $position_latitude.val('');
            $alcaldia.val('');
            $vehicle_current_status.val('');
            $position_speed.val('');
        },
        update_editor: function(metrobus) {
            $metrobus_id.val(metrobus.metrobus_id);
            $update_time.val(metrobus.update_time),
            $vehicle_id.val(metrobus.vehicle_id).focus();
            $geographic_point.val(metrobus.geographic_point);
            $position_longitude.val(metrobus.position_longitude);
            $position_latitude.val(metrobus.position_latitude);
            $alcaldia.val(metrobus.alcaldia);
            $vehicle_current_status.val(metrobus.vehicle_current_status);
            $position_speed.val(metrobus.position_speed);
        },
        build_table: function(metrobus) {
            let rows = ''

            $('.metrobus table > tbody').empty();

            // did we get a people array?
            if (metrobus) {
                for (let i=0, l=metrobus.length; i < l; i++) {
                    rows += `<tr data-metrobus-id="${metrobus[i].metrobus_id}">
                        <td class="update_time">${metrobus[i].update_time}</td>
                        <td class="vehicle_id">${metrobus[i].vehicle_id}</td>
                        <td class="geographic_point">${metrobus[i].geographic_point}</td>
                        <td class="position_longitude">${metrobus[i].position_longitude}</td>
                        <td class="position_latitude">${metrobus[i].position_latitude}</td>
                        <td class="alcaldia">${metrobus[i].alcaldia}</td>
                        <td class="vehicle_current_status">${metrobus[i].vehicle_current_status}</td>
                        <td class="position_speed">${metrobus[i].position_speed}</td>
                    </tr>`;
                }
                $('table > tbody').append(rows);
            }
        },
        error: function(error_msg) {
            $('.error')
                .text(error_msg)
                .css('visibility', 'visible');
            setTimeout(function() {
                $('.error').css('visibility', 'hidden');
            }, 3000)
        }
    };
}());

// Crea el controlador
ns.controller = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body'),
        $metrobus_id = $('#metrobus_id'),
        $update_time = $('#update_time'),
        $vehicle_id = $('#vehicle_id');
        $geographic_point = $('#geographic_point');
        $position_longitude = $('#position_longitude');
        $position_latitude = $('#position_latitude');
        $alcaldia = $('#alcaldia');
        $vehicle_current_status = $('#vehicle_current_status');
        $position_speed = $('#position_speed');

    setTimeout(function() {
        model.read();
    }, 100)

    $('table > tbody').on('dblclick', 'tr', function(e) {
        let $target = $(e.target),
            metrobus_id,
            update_time,
            vehicle_id,
            geographic_point,
            position_longitude,
            position_latitude,
            alcaldia,
            vehicle_current_status,
            position_speed;

        metrobus_id = $target
            .parent()
            .attr('data-metrobus-id');

        update_time = $target
            .parent()
            .find('td.update_time')
            .text();

        vehicle_id = $target
            .parent()
            .find('td.vehicle_id')
            .text();

        geographic_point = $target
            .parent()
            .find('td.geographic_point')
            .text();

        position_longitude = $target
            .parent()
            .find('td.position_longitude')
            .text();

        position_latitude = $target
            .parent()
            .find('td.position_latitude')
            .text();

        alcaldia = $target
            .parent()
            .find('td.alcaldia')
            .text();

        vehicle_current_status = $target
            .parent()
            .find('td.vehicle_current_status')
            .text();

        position_speed = $target
            .parent()
            .find('td.position_speed')
            .text();

        view.update_editor({
            metrobus_id: metrobus_id,
            update_time: update_time,
            vehicle_id: vehicle_id,
            geographic_point: geographic_point,
            position_longitude: position_longitude,
            position_latitude: position_latitude,
            alcaldia: alcaldia,
            vehicle_current_status: vehicle_current_status,
            position_speed: position_speed,
        });
    });

    // Handle the model events
    $event_pump.on('model_read_success', function(e, data) {
        view.build_table(data);
        view.reset();
    });

    $event_pump.on('model_create_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_update_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_delete_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_error', function(e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
        view.error(error_msg);
        console.log(error_msg);
    })
}(ns.model, ns.view));