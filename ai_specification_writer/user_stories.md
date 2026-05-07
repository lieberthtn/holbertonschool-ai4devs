# User Stories for CarpoolConnect

## User Story 1
**As a** Employee (Driver/Passenger), **I want to** log in using my corporate email **so that** I can access the trusted platform and ensure all participants are my colleagues.
- **Acceptance Criteria 1**: System validates the email domain against the approved corporate list.
- **Acceptance Criteria 2**: User receives a verification link or uses SSO.
**Priority**: MVP

## User Story 2
**As a** Driver, **I want to** post my commuting route and schedule **so that** potential passengers can see when and where I am driving.
- **Acceptance Criteria 1**: Driver can set pickup point, destination, and departure time.
- **Acceptance Criteria 2**: Driver can specify the number of available seats.
**Priority**: MVP

## User Story 3
**As a** Passenger, **I want to** search for rides by destination and time **so that** I can find a colleague who is heading to the same office.
- **Acceptance Criteria 1**: System filters results based on office location and arrival time.
- **Acceptance Criteria 2**: Results are sorted by proximity to the passenger's home.
**Priority**: MVP

## User Story 4
**As a** Passenger, **I want to** request a seat in a colleague's car **so that** I can secure my spot for the commute.
- **Acceptance Criteria 1**: Driver receives a real-time notification of the request.
- **Acceptance Criteria 2**: Driver can accept or decline the request within the app.
**Priority**: MVP

## User Story 5
**As a** Passenger, **I want to** use the system to automatically calculate and transfer fuel costs **so that** I don't have to handle awkward cash transactions with colleagues.
- **Acceptance Criteria 1**: System calculates cost based on mileage and pre-defined fuel rates.
- **Acceptance Criteria 2**: Payment is processed only after the ride is marked as completed.
**Priority**: High

## User Story 6
**As a** Employee, **I want to** see how much CO2 I have saved by carpooling **so that** I can track my contribution to the company's sustainability goals.
- **Acceptance Criteria 1**: Dashboard displays "Kg of CO2 saved" based on trip distance.
- **Acceptance Criteria 2**: Statistics can be shared on the internal corporate portal.
**Priority**: Medium

## User Story 7
**As a** Driver, **I want to** use integrated GPS navigation for the carpool route **so that** I can pick up all passengers efficiently without switching apps.
- **Acceptance Criteria 1**: The map shows the optimal route with all pickup stops included.
- **Acceptance Criteria 2**: Real-time traffic updates are integrated.
**Priority**: Medium

## User Story 8
**As a** User (Driver/Passenger), **I want to** have an SOS button that alerts corporate security **so that** I feel safe during the commute in case of an emergency.
- **Acceptance Criteria 1**: One-tap button sends current GPS location to the company security desk.
- **Acceptance Criteria 2**: App records the last 30 seconds of audio when triggered.
**Priority**: High

## User Story 9
**As a** Corporate Admin, **I want to** see a summary of platform usage across the company **so that** I can report on environmental impact and employee engagement.
- **Acceptance Criteria 1**: Admin can see total rides completed and total CO2 saved.
- **Acceptance Criteria 2**: Admin can manage (add/remove) employee access.
**Priority**: Medium

## User Story 10
**As a** Driver, **I want to** set my schedule as "Recurring" for the whole week **so that** I don't have to manually create a new ride every day.
- **Acceptance Criteria 1**: Option to select days of the week (e.g., Mon-Fri).
- **Acceptance Criteria 2**: System automatically generates trips 24 hours in advance.
**Priority**: Low

## User Story 11
**As a** Passenger, **I want to** rate my ride and the driver **so that** other colleagues know which rides are the most reliable.
- **Acceptance Criteria 1**: Rating scale from 1 to 5 stars must be available.
- **Acceptance Criteria 2**: Option to add a short text review is provided.
**Priority**: Medium

## User Story 12
**As a** Driver, **I want to** set a "Ladies Only" preference for my rides **so that** I can feel more comfortable and safe during my commute.
- **Acceptance Criteria 1**: Driver can toggle gender preferences in trip settings.
- **Acceptance Criteria 2**: System filters out requests that do not match the preference.
**Priority**: Low
