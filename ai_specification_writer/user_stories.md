# User Stories for CarpoolConnect

### User Story 1: Employee Authentication
**Role**: Employee (Driver/Passenger)
**Goal**: I want to log in using my corporate email.
**Benefit**: So that I can access the trusted platform and ensure all participants are my colleagues.
**Acceptance Criteria**:
- System validates the email domain against the approved corporate list.
- User receives a verification link or uses SSO.
**Priority**: MVP

### User Story 2: Ride Creation
**Role**: Driver
**Goal**: I want to post my commuting route and schedule.
**Benefit**: So that potential passengers can see when and where I am driving.
**Acceptance Criteria**:
- Driver can set pickup point, destination, and departure time.
- Driver can specify the number of available seats.
**Priority**: MVP

### User Story 3: Ride Search
**Role**: Passenger
**Goal**: I want to search for rides by destination and time.
**Benefit**: So that I can find a colleague who is heading to the same office.
**Acceptance Criteria**:
- System filters results based on office location and arrival time.
- Results are sorted by proximity to the passenger's home.
**Priority**: MVP

### User Story 4: Booking Request
**Role**: Passenger
**Goal**: I want to request a seat in a colleague's car.
**Benefit**: So that I can secure my spot for the commute.
**Acceptance Criteria**:
- Driver receives a real-time notification of the request.
- Driver can accept or decline the request within the app.
**Priority**: MVP

### User Story 5: Cost Sharing
**Role**: Passenger
**Goal**: I want the system to automatically calculate and transfer fuel costs.
**Benefit**: So that I don't have to handle awkward cash transactions with colleagues.
**Acceptance Criteria**:
- System calculates cost based on mileage and pre-defined fuel rates.
- Payment is processed only after the ride is marked as completed.
**Priority**: High

### User Story 6: Carbon Footprint Tracking
**Role**: Employee
**Goal**: I want to see how much CO2 I have saved by carpooling.
**Benefit**: So that I can track my contribution to the company's sustainability goals.
**Acceptance Criteria**:
- Dashboard displays "Kg of CO2 saved" based on trip distance.
- Statistics can be shared on the internal corporate portal.
**Priority**: Medium

### User Story 7: Real-time Navigation
**Role**: Driver
**Goal**: I want integrated GPS navigation for the carpool route.
**Benefit**: So that I can pick up all passengers efficiently without switching apps.
**Acceptance Criteria**:
- The map shows the optimal route with all pickup stops included.
- Real-time traffic updates are integrated.
**Priority**: Medium

### User Story 8: Emergency Button
**Role**: User (Driver/Passenger)
**Goal**: I want an SOS button that alerts corporate security.
**Benefit**: So that I feel safe during the commute in case of an accident or emergency.
**Acceptance Criteria**:
- One-tap button sends current GPS location to the company security desk.
- App records the last 30 seconds of audio when triggered.
**Priority**: High

### User Story 9: Admin Dashboard
**Role**: Corporate Admin
**Goal**: I want to see a summary of platform usage across the company.
**Benefit**: So that I can report on environmental impact and employee engagement.
**Acceptance Criteria**:
- Admin can see total rides completed and total CO2 saved.
- Admin can manage (add/remove) employee access.
**Priority**: Medium

### User Story 10: Recurring Rides
**Role**: Driver
**Goal**: I want to set my schedule as "Recurring" for the whole week.
**Benefit**: So that I don't have to manually create a new ride every day.
**Acceptance Criteria**:
- Option to select days of the week (e.g., Mon-Fri).
- System automatically generates trips 24 hours in advance.
**Priority**: Low
