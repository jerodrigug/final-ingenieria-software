import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ValidateDocComponent } from './validate-doc.component';

describe('ValidateDocComponent', () => {
  let component: ValidateDocComponent;
  let fixture: ComponentFixture<ValidateDocComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ValidateDocComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ValidateDocComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
